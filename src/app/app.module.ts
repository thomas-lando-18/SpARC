import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { MatTab, MatTabGroup } from '@angular/material/tabs';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { SimulatorComponent } from './simulator/simulator.component';
import { RocketComponent } from './rocket/rocket.component';

@NgModule({
    declarations: [
        AppComponent,
        RocketComponent,
    ],
    providers: [
        provideClientHydration(),
        provideAnimationsAsync()
    ],
    bootstrap: [AppComponent],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HeaderComponent,
        MatTab,
        MatTabGroup,
        SimulatorComponent
    ]
})
export class AppModule { }
